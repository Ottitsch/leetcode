library(NLP)

# Sample text
text <- "I love writing fun little R scripts with the NLP package. 
         NLP makes text mining fun, simple, and powerful. 
         Let's play with words and frequencies!"

# Create an NLP string object
s <- as.String(text)

# Use a simple regex to tokenize into words
words <- unlist(strsplit(as.character(s), "\\W+"))
words <- tolower(words)
words <- words[words != ""]  # drop empties

# Count word frequencies
word_freq <- sort(table(words), decreasing = TRUE)

# Print frequencies
print(word_freq)

# Make a fun text-based "word cloud"
cat("\n=== Text Cloud ===\n")
for (w in names(word_freq)) {
  count <- word_freq[[w]]
  cat(rep(w, count), sep = " ", "\n")
}

