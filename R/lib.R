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
  cutree(hclust_avg, 3)

  dendrogramFileName <- paste0(rootFolder, "/", french, "Dendrogram.png")
  png(dendrogramFileName)

  return(hclust_avg)
}

write_cluster_graph <- function(hclust_avg, kmax) {
  plot(hclust_avg,
    cex = 1)
  rect.hclust(hclust_avg, k = kmax)
}
