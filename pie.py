import matplotlib.pyplot as plt

def make_pie_chart(labels, sizes, filename="chart"):
    explode = [0.1 if size > 20 else 0 for size in sizes]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig(f"./images/{filename}.png")
