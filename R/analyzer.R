library(dplyr)
library(readxl)
library(stringr)
library(stringdist)
library(data.table)
library(ggplot2)
library(ggrepel)
library(factoextra)
library(gsubfn)
source("R/lib.R")

rootFolder <- "./output"
data <- read_data(paste(rootFolder, "normalized.csv", sep = "/"))

# TODO: small set for testing, we need a better solution
# rootFolder <- "./testOutput"
# unlink(rootFolder, recursive=TRUE)
# dir.create('./testOutput')
# data <- read_data( "test/tenLinesNormalizedFile.csv")

errors <- c()
languages <- c("swo", "gyeli", "bekwel", "bekol", "konzime", "makaa", "mpiemo", "kwasio", "njem", "shiwa")

write_graphs <- function(data) {
  tryCatch({
    french_word <- get_french_word(data)
    print(paste0("start: ", french_word))

    cleaned_up_words <- clean_up_word_data(data)
    languages <- cleaned_up_words$languages
    the_word <- cleaned_up_words$the_word

    dist_mat <- calculate_distance_matrix(the_word, languages)

    write_distance_graph(dist_mat, french_word)
    write_cluster_graph(dist_mat, french_word, languages)
    write_dendrogram_graph(dist_mat, french_word, languages)

    print(paste0("done: ", french_word))
  },
    error = function(e) {
      message('An Error Occurred')
      print(e)
      assign("errors", c(french_word, errors), envir = .GlobalEnv)
      print(c("error: ", errors))
      print("end ex handler")
    },
    warning = function(w) {
      message('A Warning Occurred')
      print(w)
      assign("errors", c(french_word, errors), envir = .GlobalEnv)
      print(c("warning: ", errors))
      print("end ex handler")
      return(NA)
    }
  )
}

sapply(data[, 2:ncol(data)], write_graphs)

print(c("errors", errors))
print("done")
