library(dplyr)
library(readxl)
library(stringr)
library(stringdist)
library(data.table)
library(ggplot2)
library(ggrepel)
library(factoextra)
library(gsubfn)

# rootFolder <- "./output"
rootFolder <- "./testOutput"


## Functions
# TODO: move to file?

read_data <- function(filename) {
  data <- fread(filename) %>%
    t() %>%
    as.data.frame()

  # change the first row to be column names
  colnames(data) <- data[2,]

  # remove the column header row
  data <- data[-1,]

  # add language names as the first column
  data$Language <- rownames(data)
  data <- data %>% select(Language, everything())

  colnames(data) <- colnames(data) %>% str_replace(" ", "_")

  # Only keep data about a language, remove all other columns
  data <- data[-c(2, 13, 14, 15),]

  return(data)
}

get_french_word <- function(data) {
  french <- sub(" ", "_", data[1])
  french <- sub("/", "_", french)
  french <- sub("\\(", "_", french)
  french <- sub("\\)", "_", french)

  return(french)
}

clean_up_word_data <- function(data) {
  the_word <- data[-1]
  nonEmptyWords <- data.frame(languages, the_word)
  nonEmptyWords <- nonEmptyWords %>% filter(!(the_word %in% c("", "NA")))

  return(nonEmptyWords)
}

calculate_distance_matrix <- function(the_word, languages) {
  dist_mat <- stringdist::stringdistmatrix(the_word, the_word,
                                           method = "lv",
                                           useNames = "string")

  # normalize levenshtein distance
  for (i in seq_len(ncol(dist_mat))) {
    for (z in seq_len(nrow(dist_mat))) {
      dist_mat[z, i] <- dist_mat[z, i] / max(str_count(colnames(dist_mat)[i]),
                                             str_count(rownames(dist_mat)[z]))
    }
  }

  rownames(dist_mat) <- languages
  colnames(dist_mat) <- languages
  dist_mat <- dist_mat %>% replace(is.na(.), 0)

  return (dist_mat)
}

write_distance_graph <- function(dist_mat, french) {
  # change the distances to multidimensional scaling
  fit <- cmdscale(dist_mat,
                  eig = TRUE,
                  k = 2)

  # extract the two dimensions
  cbind(fit$points[, 1], fit$points[, 2]) %>%
    as.data.frame() %>%
    rename(x = 1, y = 2) %>%
    mutate(Name = colnames(dist_mat)) %>%
    ggplot(aes(x = x, y = y, label = Name)) +
    geom_text_repel(max.overlaps = Inf) +
    theme_bw() +
    theme(legend.position = "top")

  distanceFileName <- paste0(rootFolder, "/", french, "Distance.png")
  ggsave(distanceFileName, width = 10, height = 10, units = "cm")
}

write_dendrogram <- function(dist_mat, french, kmax) {
  dist_mat <- dist_mat
  fviz_nbclust(dist_mat, FUN = hcut, method = "silhouette", k.max = kmax)
  clusterFileName <- paste0(rootFolder, "/", french, "NoOfClusters.png")
  ggsave(clusterFileName, width = 10, height = 10, units = "cm")

  hclust_avg <- hclust(dist_mat %>% as.dist())
  clus <- cutree(hclust_avg, 3)

  test <- clus %>%
    as.data.frame() %>%
    rename(Cluster = 1) %>%
    mutate(Name = names(clus))

  # match the order of rows in the data with the order of tip labels
  test <- test[match(names(clus), test$Name),]

  dendrogramFileName <- paste0(rootFolder, "/", french, "Dendrogram.png")
  png(dendrogramFileName)
  return(hclust_avg)
}

write_cluster_graph <- function(hclust_avg, kmax) {
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
}

## Main

# data <- read_data(paste(rootFolder, "normalized.csv", sep = "/"))
data <- read_data( "test/tenLinesNormalizedFile.csv")
errors <- c()
languages <- c("swo", "gyeli", "bekwel", "bekol", "konzime", "makaa", "mpiemo", "kwasio", "njem", "shiwa")

write_graphs <- function(data) {
  french <- get_french_word(data)
  print(paste0("start: ", french))

  cleaned_up_words <- clean_up_word_data(data)
  languages <- cleaned_up_words$languages
  the_word <- cleaned_up_words$the_word

  dist_mat <- calculate_distance_matrix(the_word, languages)
  kmax <- length(languages) - 1

  tryCatch({
    write_distance_graph(dist_mat, french)
    hclust_avg <- write_dendrogram(dist_mat, french, kmax)
    write_cluster_graph(hclust_avg, kmax)

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



