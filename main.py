# main.py

from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
import matplotlib.pyplot as plt

def main():
    # Generate and show line plot
    fig1 = draw_line_plot()
    plt.show()
    
    # Generate and show bar plot
    fig2 = draw_bar_plot()
    plt.show()
    
    # Generate and show box plots
    fig3 = draw_box_plot()
    plt.show()

if __name__ == "__main__":
    main()
