"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    
    os.makedirs(os.path.dirname("files/plots/news.png"), exist_ok=True)
    
    plt.Figure()
    
    colors = {"Television":"dimgray",
            "Newspaper": "grey",
            "Internet": "tab:blue",
            "Radio": "Lightgrey",
            }
    
    zorder = {"Television": 1,
            "Newspaper": 1,
            "Internet": 2,
            "Radio": 1,
            }
    
    linewidths = {"Television": 2,
            "Newspaper": 2,
            "Internet": 4,
            "Radio": 2,
            }

    df = pd.read_csv("files/input/news.csv", index_col=0)
    
    for column in df.columns:
        plt.plot(
            df[column], 
            color=colors[column],
            label=column,
            zorder=zorder[column],
            linewidth=linewidths[column],
            )

    plt.title("How people get their news", fontsize=16)

    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for column in df.columns:
        first_year = df[column].index[0]
        plt.scatter(
            x=first_year,
            y=df[column][first_year],
            color=colors[column],
            zorder=zorder[column],
        )

        plt.text(
            first_year -0.2,
            df[column][first_year],
            column + " "+ str(df[column][first_year]) + "%",
            ha = "right",
            va = "center",
            color = colors[column],
        )


        last_year = df[column].index[-1]
        plt.scatter(
            x=last_year,
            y=df[column][last_year],
            color=colors[column],
            zorder=zorder[column],
        )

        plt.text(
            last_year + 0.2,
            df[column][last_year],
            str(df[column][last_year]) + "%",
            ha = "left",
            va = "center",
            color = colors[column],
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha = "center",
    )
    
    plt.savefig("files/plots/news.png")
    plt.show()

    return 0
    
if __name__ == "__main__":
    pregunta_01()