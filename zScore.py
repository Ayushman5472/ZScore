import plotly.figure_factory as ff
import pandas as pd
import statistics 
import random
import plotly.graph_objects as go

data = pd.read_csv('data.csv')
data = data['Math_score'].tolist()

data1 = pd.read_csv('data1.csv')
data1 = data1['Math_score'].tolist()

data2 = pd.read_csv('data2.csv')
data2 = data2['Math_score'].tolist()

data3 = pd.read_csv('data3.csv')
data3 = data3['Math_score'].tolist()

Mean = statistics.mean(data)
#print(Mean)

Stdev = statistics.stdev(data)
#print(Stdev)

def Sampling(Number):
    dataSet = []
    for i in range(0,Number):
        index = random.randint(0,len(data)-1)
        Value = data[index]
        dataSet.append(float(Value))
    Mean = statistics.mean(dataSet)
    return(Mean)

MeanList = []
for i in range(0,1000):
    SamplingValue = Sampling(100)
    MeanList.append(float(SamplingValue))

SamplingMean = statistics.mean(MeanList)
print(SamplingMean)

SamplingStdev = statistics.stdev(MeanList)
print(SamplingStdev)

FirstSt_Start, FirstSt_End = SamplingMean + SamplingStdev, SamplingMean-SamplingStdev
SecondSt_Start, SecondSt_End = SamplingMean + 2*SamplingStdev, SamplingMean - 2*SamplingStdev
ThirdSt_Start, ThirdSt_End = SamplingMean + 3*SamplingStdev, SamplingMean - 3*SamplingStdev

data1Mean = statistics.mean(data1)
data2Mean = statistics.mean(data2)
data3Mean = statistics.mean(data3)

graph = ff.create_distplot([MeanList], ['Sampling Distribution'], show_hist = False)
graph.add_trace(go.Scatter(x = [SamplingMean, SamplingMean], y = [0,1], mode = "lines", name = "Mean" ))
graph.add_trace(go.Scatter(x =[FirstSt_Start, FirstSt_Start], y = [0,1], mode = "lines", name = "First Standard Deviation Start"))
graph.add_trace(go.Scatter(x = [FirstSt_End, FirstSt_End], y = [0,1], mode = 'lines', name = "First Standard Deviation End"))
graph.add_trace(go.Scatter(x = [SecondSt_Start,SecondSt_Start], y = [0,1], mode = 'lines', name = "Second Standard Deviation Start"))
graph.add_trace(go.Scatter(x = [SecondSt_End, SecondSt_End], y = [0,1], mode = 'lines', name = "Second Standard Deviation End"))
graph.add_trace(go.Scatter(x = [ThirdSt_Start, ThirdSt_Start], y = [0,1], mode = 'lines', name = "Third Standard Deviation Start"))
graph.add_trace(go.Scatter(x = [ThirdSt_End, ThirdSt_End], y = [0,1], mode = 'lines', name = "Third Standard Deviation End"))
graph.add_trace(go.Scatter(x = [data1Mean, data1Mean], y = [0,1], mode = 'lines', name = "data1 Mean"))
graph.add_trace(go.Scatter(x = [data2Mean, data2Mean], y = [0,1], mode = 'lines', name = "data2 Mean"))
graph.add_trace(go.Scatter(x = [data3Mean, data3Mean], y = [0,1], mode = 'lines', name = "data3 Mean"))
#graph.show()

zScore_data1 = (data1Mean - SamplingMean)/SamplingStdev
zScore_data2 = (data2Mean - SamplingMean)/SamplingStdev
zScore_data3 = (data3Mean - SamplingMean)/SamplingStdev
print(zScore_data1)
print(zScore_data2)
print(zScore_data3)