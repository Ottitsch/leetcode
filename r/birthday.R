library(ggplot2); library(scales)

N <- 75; days <- 365; targets <- c(.50, .99)

k    <- 0:(N-1)
p_no <- exp(cumsum(log1p(-k/days)))          # stable log-space
df   <- data.frame(n = 1:N, prob = 1 - p_no)

idx  <- sapply(targets, function(t) which(df$prob >= t)[1])
hits <- data.frame(target = targets, n = idx, prob = df$prob[idx])

p <- ggplot(df, aes(n, prob)) +
  geom_line(linewidth = 1) +
  geom_vline(data = hits, aes(xintercept = n), linetype = 2) +
  geom_hline(data = hits, aes(yintercept = prob), linetype = 2) +
  geom_point(data = hits, aes(n, prob), size = 3) +
  scale_y_continuous(labels = label_percent(1), limits = c(0, 1)) +
  labs(title = "Birthday problem",
       subtitle = paste("P(at least one match),", days, "days"),
       x = "Group size (n)", y = "Probability")

if (interactive()) print(p) else {
  ggsave("birthday.png", p, width = 8, height = 5, dpi = 160)
  write.csv(df, "birthday_results.csv", row.names = FALSE)
}

