#' Read the word data from a csv file and transform into a data frame
#'
#' @param filename The name of the csv file
#' @returns Dataframe with the data
read_data <- function(filename) {
  data <- fread(filename) %>%
    t() %>%
    as.data.frame()

  # set words as column headers
  colnames(data) <- data[2,]

  # remove column numbers
  data <- data[-1,]

  # add language names as the first column
  data$Language <- rownames(data)
  data <- data %>% select(Language, everything())

  colnames(data) <- colnames(data) %>% str_replace(" ", "_")

  # Only keep data about a language, remove all other columns
  data <- data[-c(2, 13, 14, 15),]

  return(data)
}

#' Get the French word from the data we have about a word, replacing spaces, slashes and parenthesis to avoid problems later
#'
#' @param Data frame with the Franch word in column 1
#' @returns Cleaned up Franch word
get_french_word <- function(data) {
  french <- sub(" ", "_", data[1])
  french <- sub("/", "_", french)
  french <- sub("\\(", "_", french)
  french <- sub("\\)", "_", french)

  return(french)
}

#' Remove French word and all empty columns from the data frame
#'
#' @param data Data frame for a word
#' @returns Data frame without the French word and without empty columns
clean_up_word_data <- function(data) {
  the_word <- data[-1]
  nonEmptyWords <- data.frame(languages, the_word)
  nonEmptyWords <- nonEmptyWords %>% filter(!(the_word %in% c("", "NA")))

  return(nonEmptyWords)
}

#' Calculate the normalized (0 to 1) distance between translations of the word and return as a distance matrix
#'
#' @param the_word  Word in several languages
#' @param languages List of languages
#' @returns normalized distance matrix using Levenshtein
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

#' Create a graph of the distance matrix
#'
#' @param dist_mat normalized distance matrix
#' @param french_word french word, used to construct a name for the output file
write_distance_graph <- function(dist_mat, french_word) {
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

  distanceFileName <- paste0(rootFolder, "/", french_word, "Distance.png")
  ggsave(distanceFileName, width = 10, height = 10, units = "cm")
}

#' Create number of clusters plot of the distance matrix
#'
#' @param dist_mat normalized distance matrix
#' @param french_word french word, used to construct a name for the output file
#' @param languages List of languages
write_cluster_graph <- function(dist_mat, french_word, languages) {
  kmax <- length(languages) - 1
  dist_mat <- dist_mat
  fviz_nbclust(dist_mat, FUN = hcut, method = "silhouette", k.max = kmax)
  clusterFileName <- paste0(rootFolder, "/", french_word, "NoOfClusters.png")
  ggsave(clusterFileName, width = 10, height = 10, units = "cm")
}

#' Create dendogram graph of the distance matrix
#'
#' @param dist_mat normalized distance matrix
#' @param french_word french word, used to construct a name for the output file
#' @param languages List of languages
write_dendrogram_graph <- function(dist_mat, french_word, languages) {
  dendrogramFileName <- paste0(rootFolder, "/", french_word, "Dendrogram.png")
  png(dendrogramFileName)

  hclust_avg <- hclust(dist_mat %>% as.dist())
  cutree(hclust_avg, 3)
  kmax <- length(languages) - 1
  plot(hclust_avg, cex = 1)
  rect.hclust(hclust_avg, k = kmax)

  dev.off()

}
