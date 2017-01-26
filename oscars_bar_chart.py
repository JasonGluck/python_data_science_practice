from matplotlib import pyplot as plt

def oscars_bar_chart():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    xs = [ i + 0.1 for i, _ in enumerate(movies)]
    plt.bar(xs, num_oscars)
    plt.ylabel("# of Oscars")
    plt.title("My Favorite Movies")
    plt.xticks([i + 0.10 for i, _ in enumerate(movies)], movies)
    plt.show()

oscars_bar_chart()
