from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .forms import ProcessForm
from .models import Process
from .srtnalgo import Process_Algo,srtn
from .sstf_algo import sstf
from .page_replacement import optimalPageReplacement
import plotly.graph_objects as go


# Create your views here.
def home(request):
    return render(request,'Simulator/index.html')

def SRTN(request):
    Processes = Process.objects.all()
    if request.method == 'POST':
        form = ProcessForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Process_name']
            at = form.cleaned_data['Arrival_time']
            bt = form.cleaned_data['Burst_time']
            reg = Process(Process_name=name,
                          Arrival_time=at,
                          Burst_time=bt)
            reg.save()
        else:
            Process.objects.all().delete()
    form = ProcessForm()
    context = {'form':form,'processes':Processes}
    return render(request,'Simulator/srtn.html',context=context)

def SRTN_result(request):    
    Processes = Process.objects.all()
    Processes_Algo = []
    
    for i in Processes:
        Processes_Algo.append(Process_Algo(i.Process_name,i.Arrival_time,i.Burst_time,0,0.00,0))
    
    Output=srtn(Processes_Algo)
    Gantt_Chart = Output.pop(-1)
    context={'processes':Output,'Gantt_Chart':Gantt_Chart}
    return render(request,'Simulator/srtn_result.html',context=context)

buffer_size=0
current_item=-1
buff_list=[]
def Producer_consumer(request):
    global buffer_size
    global buff_list
    global current_item
    prod_msg=""
    cons_msg=""
    producing=False
    consuming=False

    if request.method == 'POST':
        if request.POST.get('buffer_size'):
            buffer_size = int(request.POST.get('buffer_size',buffer_size))
            current_item=-1
            buff_list=[]
            for i in range(buffer_size):
                buff_list.append("---")
        
        elif request.POST.get('produce'):
            if(current_item==buffer_size-1):
                prod_msg="Can't Produce!! Buffer is Full"
            else:
                producing=True
                current_item+=1
                buff_list[current_item]="Item"+str(current_item)
                prod_msg=buff_list[current_item]+" produced"
            
        
        elif request.POST.get('consume'):
            if(current_item==-1):
                cons_msg="Can't Consume!! Buffer is Empty"
            else:
                consuming=True
                cons_msg=buff_list[current_item]+" consumed"
                buff_list[current_item]="---"
                current_item-=1
    print(producing)       
    return render(request,"Simulator/producer_consumer.html",context={"buffer":buffer_size,"buff_list":buff_list,"prod_msg":prod_msg,"producing":producing,"consuming":consuming,"cons_msg":cons_msg})

head_pointer = None
disk_request_seq=[]
def SSTF(request):
    global head_pointer
    global disk_request_seq
    error = 0
    chart = None
    no_of_cylinders=-1
    output=[]
    if request.method == 'POST':
        if request.POST.get('head_pointer'):
            head_pointer = int(request.POST.get('head_pointer'))
            disk_request_seq = []
    
        elif request.POST.get('disk'):
            disk = int(request.POST.get('disk'))
            if(disk>=0):
                disk_request_seq.append(disk)
            else:
                error=1
        
        elif request.POST.get('run'):
            disk_req = disk_request_seq.copy()
            result = sstf(disk_req,head_pointer)
            no_of_cylinders = result[-1]
            output = result[0]
            # print(output)
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=result[0], 
                y=[i for i in range(len(result[0]))], 
                mode='lines+markers',
                marker=dict(
                    symbol="arrow",
                    size=15,
                    angleref="previous"
                )
            ))
           
            fig.update_yaxes(visible=False, fixedrange=True)
            fig.update_xaxes(
                tickvals=disk_request_seq.sort(),
            )
            fig.update_layout(
                title=dict(text='Result')
            )
            chart = fig.to_html()
            

        elif request.POST.get('new'):
            head_pointer=''
            disk_request_seq=[]

    return render(request,"Simulator/sstf.html",context={'head_pointer':head_pointer,'error':error,'disk_seq':disk_request_seq,'output':output, 'chart':chart, 'no_of_cylinders':no_of_cylinders})

frame_size=0
pages=[]
def PageReplacement(request):
    global pages
    global frame_size
    error=0
    output=()
    hit=0
    frames=[]
    frames_dict={}

    if request.method == 'POST':
        if request.POST.get('frame_size'):
            frame_size = int(request.POST.get('frame_size'))
            pages = []
        
        elif request.POST.get('page'):
            page = int(request.POST.get('page'))
            if(page>=0):
                pages.append(page)
            else:
                error=1
        
        elif request.POST.get('new'):
            frame_size = 0
            pages = []

        elif request.POST.get('run'):
            output = optimalPageReplacement(pages, frame_size)
            hit = output[0]
            frames = output[1]
            frames_dict={}
            for i in range(len(pages)):
                tup=(i,pages[i])
                frames_dict[tup]=frames[i]
               
    return render(request,"Simulator/pagereplacement.html",context={'fn':frame_size,'pages':pages,'error':error,'hit':hit,'frames':frames,'output':output,'frames_dict':frames_dict})