import matplotlib.pyplot as plt

def save_bias_chart(confidences, filename="bias_chart.png"):
    plt.bar(confidences.keys(), confidences.values(), color=['red', 'gray', 'blue'])
    plt.title("Bias Prediction Confidence")
    plt.savefig(filename)
    plt.close()

def save_sentiment_chart(polarity, filename="sentiment_chart.png"):
    plt.barh(["Sentiment"], [polarity], color="green" if polarity > 0 else "red")
    plt.title("Sentiment Polarity")
    plt.savefig(filename)
    plt.close()
