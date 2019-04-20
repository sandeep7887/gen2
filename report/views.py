from django.shortcuts import render
from django.http import HttpResponse
from report.models import *
# Create your views here.

def status(request,status_id):
    # print(status_id)
    details = execution_details.objects.filter(id=status_id).values('project','test_type','execution_date')
    run_result = execution_summary.objects.filter(reference_id=status_id).values('tcname','suite','status')
    # print('details: ',details)
    # print('result: ',run_result)
    Executed=0;Passed=0;Failed=0;Others=0;Notexecuted=0
    for i in run_result:
        if i['status'] == 'Passed':
            Passed+=1
        elif i['status'] == 'Failed':
            Failed+=1
        elif i['status'] == 'Not-executed':
            Notexecuted+=1
        elif (i['status'] != 'In-progress') and (i['status'] != 'Failed') and (i['status'] != 'Passed') and (i['status'] != 'Not-executed'):
            Others+=1
    Executed = Passed + Failed + Others
    ll = [Executed,Passed,Failed,Others,Notexecuted]
    print(len(run_result))
    return render(request, 'index.html',{'status_id':status_id,'bar':ll,'pie':ll[1:-1],'details':details[0],'result':run_result})
