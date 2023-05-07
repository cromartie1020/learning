from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import EntryForm, TopicForm 
def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics=Topic.objects.all()
    context={
        'topics':topics
    }
    return render(request,'learning_logs/topics.html',context)

def topic(request, topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context={
        'topic':topic,
        'entries':entries
    }    
    return render(request, 'learning_logs/topic.html',context)

def new_topic(request):
    if request.method=='POST':
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')

    else:
        form=TopicForm()    
    context={
        "form":form
    }
    return render(request,'learning_logs/new_topic.html',context)

def new_entry(request, topic_id):
    topic=Topic.objects.get(id=topic_id)
    if request.method=='POST':
        
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            
            return redirect('topics')
    else:
        form=EntryForm()
    context={
        "form":form,   
        "topic":topic,
        
    }        
    return render(request, 'learning_logs/new_entry.html',context)

def edit_entry(request, entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method=='POST':
        
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            
            
            return redirect('topics')
    else:
        form=EntryForm(instance=entry)
    context={
        "form":form,   
        "entry":entry,
        "topic":topic
        
    }        
    return render(request, 'learning_logs/edit_entry.html',context)
