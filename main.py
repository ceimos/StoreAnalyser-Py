import os
import sys
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

plt.style.use('dark_background')

def getSize(path = '.'):
    total_size = 0
    try : 
        for (dirpath, dirnames, filenames) in os.walk(path):
            try :
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            except : 
                continue
    except : 
        print("Something Went wrong while traversing ", path)
    return total_size

def show():
    image=Image.open('./visualization.png')
    image.show()

def visualize(sizes : dict) :
    #colours = mcolors.mcolors.CSS4_COLORS
    colours = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#1a55FF"]
    sorted_sizes = sorted(sizes.items(), key = lambda x : x[1], reverse=True)
    top_11 = dict(sorted_sizes[:10]) #11th is added in the next line.
    top_11.update({"others" : sum(sizes.values()) - sum(top_11.values())})
    plt.pie(top_11.values(), labels = top_11.keys(), autopct='%1.0f%%', startangle=90,
            colors=colours, explode=[0.1]*len(top_11),
            labeldistance=None)
    #plt.legend(top_11.keys(), loc="upper right", bbox_to_anchor=(1.3, 0.5, 0.1, 0.3))
    plt.legend(top_11.keys(), loc="right")
    plt.show()
    plt.savefig('./visualization.png', transparent=True, dpi = 1000)

def main():
    path = sys.argv[1]
    file_list = os.listdir(path)
    sizes = {}
    for file in file_list:
        sizes.update( { file : getSize( os.path.join(path,file) ) } )
    visualize(sizes)
    show()

if __name__=="__main__":
    main()