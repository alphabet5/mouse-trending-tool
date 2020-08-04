
def onclick(event):
    global start_trend, xdata, ydata, plt, ax
    if event.button == 1:
        start_trend = not start_trend
        if start_trend:
            print("Recording...")
    if event.button == 3:
        from tkinter.filedialog import asksaveasfile
        file = asksaveasfile(mode='w',
                             defaultextension='.csv')
        try:
            file.write("xval,yval\n")
            for x in range(len(xdata)):
                file.write(str(xdata[x]) + "," + str(ydata[x]) + '\n')
            file.close()
        except:
            from traceback import format_exc
            print(format_exc())
            print("There was an error saving the file.")
        xdata = []
        ydata = []
        plt.cla()
        ax.set_xlim([0, 10])
        ax.set_ylim([0, 10])


def mouse_move(event):
    global ydata, xdata, ax, fig
    x, y = event.xdata, event.ydata
    print(x, y)
    if start_trend and x and y:
        if len(xdata) == 0:
            xdata.append(x)
            ydata.append(y)
        elif x > xdata[-1]:
            xdata.append(x)
            ydata.append(y)
    ax.plot(xdata, ydata, 'b-')
    fig.canvas.draw()


if __name__ == '__main__':
    #import matplotlib
    #matplotlib.use("TkAgg") Needed for MacOS
    from matplotlib import pyplot as plt

    fig = plt.figure(num="Mouse Plotting Tool")
    fig.suptitle('Left click to start/stop recording. Right click to save and clear.')
    ax = fig.add_subplot(111)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])

    start_trend = False
    xdata = []
    ydata = []

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.connect('motion_notify_event', mouse_move)
    plt.gcf().autofmt_xdate()
    plt.show()