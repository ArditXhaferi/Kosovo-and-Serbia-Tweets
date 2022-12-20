import matplotlib.pyplot as plt
   
def make_bar_chart(labels, sizes, filename="chart"):
    plt.bar(labels, sizes)
    plt.title('Country Vs GDP Per Capita', fontsize=14)
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('GDP Per Capita', fontsize=14)
    plt.savefig(f"./images/{filename}.png")