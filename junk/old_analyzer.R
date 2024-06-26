# install.packages("dplyr")
# install.packages('readxl')
# install.packages("stringr")
# install.packages("stringdist")
# install.packages("data.table")
# install.packages("ggplot2")
# install.packages("ggrepel")
# install.packages("factoextra")

library(dplyr)
library(readxl)
library(stringr)
library(stringdist)
library(data.table)
library(ggplot2)
library(ggrepel)
library(factoextra)

rootFolder <- "./output"
# rootFolder <- "."

# read the main table

# data <- fread(paste(rootFolder, "oneWord.csv", sep = "/")) %>%
data <- fread(paste(rootFolder, "normalized.csv", sep = "/")) %>%
  # flip the order of rows and columns
  t() %>%
  # change the format to data frame
  as.data.frame()

# change the first row to be column names
colnames(data) <- data[2,]

# remove the first row that we don't need anymore
data <- data[-1,]
# add back language names as a column
data$Language <- rownames(data)
# reorder the columns to have language first
data <- data %>% select(Language, everything())

# removing spaces in colnames
colnames(data) <- colnames(data) %>% str_replace(" ", "_")
errors <- c()

data <- data[-c(2, 13, 14, 15),]
languages <- c("swo", "gyeli", "bekwel", "bekol", "konzime", "makaa", "mpiemo", "kwasio", "njem", "shiwa")

write_graphs <- function(data) {
  french <- sub(" ", "_", data[1])
  french <- sub("/", "_", french)
  french <- sub("\\(", "_", french)
  french <- sub("\\)", "_", french)
  print(paste0("start: ", french))

  the_word <- data[-1]
  nonEmptyWords <- data.frame(languages, the_word)
  nonEmptyWords <- nonEmptyWords %>% filter(!(the_word %in% c("", "NA")))

  languages <- nonEmptyWords$languages
  the_word <- nonEmptyWords$the_word
  dist_mat <- stringdist::stringdistmatrix(the_word, the_word,
                                           method = "lv",
                                           useNames = "string")

  # normalize levenshtein distance by dividing the edit distance by the longest word in each pairwise comparison
  for (i in seq_len(ncol(dist_mat))) {
    # and for each row. The two loops mean: for each cell
    for (z in seq_len(nrow(dist_mat))) {
      # divide the lev distance by the length of the longest word between the pair of words that is being compared
      dist_mat[z, i] <- dist_mat[z, i] / max(str_count(colnames(dist_mat)[i]),
                                             str_count(rownames(dist_mat)[z]))
    }
  }

  # add row names and column names
  rownames(dist_mat) <- languages
  colnames(dist_mat) <- languages

  dist_mat <- dist_mat %>% replace(is.na(.), 0)

  # visualization
  tryCatch({
    # change the distances to multidimensional scaling
    fit <- cmdscale(dist_mat,
                    eig = TRUE,
                    # set number of dimensions
                    k = 2)

    # extract the two dimensions
    cbind(fit$points[, 1], fit$points[, 2]) %>%
      # change the formant
      as.data.frame() %>%
      # rename the columns
      rename(x = 1, y = 2) %>%
      # add metadata
      mutate(Name = colnames(dist_mat)) %>%
      # make the plot
      ggplot(aes(x = x, y = y, label = Name)) +
      # add text instead of points
      geom_text_repel(max.overlaps = Inf) +
      # white background
      theme_bw() +
      # basic plot settings
      theme(legend.position = "top")

    distanceFileName <- paste0(rootFolder, "/", french, "Distance.png")
    ggsave(distanceFileName, width = 10, height = 10, units = "cm")

    kmax <- length(languages) - 1
    fviz_nbclust(dist_mat, FUN = hcut, method = "silhouette", k.max = kmax)
    clusterFileName <- paste0(rootFolder, "/", french, "NoOfClusters.png")
    ggsave(clusterFileName, width = 10, height = 10, units = "cm")

    # save the output of clustering
    hclust_avg <- hclust(dist_mat %>% as.dist())

    # cut the data into the required number of clusters
    clus <- cutree(hclust_avg, 3)

    # change the format for a plot later
    test <- clus %>%
      # change format of the data
      as.data.frame() %>%
      # rename the column
      rename(Cluster = 1) %>%
      # add the language names
      mutate(Name = names(clus))

    # match the order of rows in the data with the order of tip labels
    test <- test[match(names(clus), test$Name),]

    dendrogramFileName <- paste0(rootFolder, "/", french, "Dendrogram.png")

    png(dendrogramFileName)

    plot( # can use this line to make the plot horizontal instead of vertical
      #ape::as.phylo(hclust_avg),
      hclust_avg,
      # change the visualization type if needed
      #type = "fan",
      # add color if needed
      #tip.color = test$Color,
      # plot settings
      #no.margin = TRUE,
      #label.offset = 0.01,
      cex = 1)
    # add squares around the clusters
    rect.hclust(hclust_avg, k = kmax)

    dev.off()
    print(paste0("done: ", french))
  },
    error = function(e) {
      message('An Error Occurred')
      print(e)
      assign("errors", c(french, errors), envir = .GlobalEnv)
      print(c("error: ", errors))
      print("end ex handler")
    },
    #if a warning occurs, tell me the warning
    warning = function(w) {
      message('A Warning Occurred')
      print(w)
      assign("errors", c(french, errors), envir = .GlobalEnv)
      print(c("warning: ", errors))
      print("end ex handler")
      return(NA)
    }
  )
}

sapply(data[, 2:ncol(data)], write_graphs)

print(c("errors", errors))
print("done")