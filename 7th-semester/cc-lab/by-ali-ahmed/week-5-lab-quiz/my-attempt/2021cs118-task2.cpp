// M YAQOOB
#include <iostream>
#include <deque>
using namespace std;

void addBackToQueue(deque<string> &tms, string task)
{
    tms.push_back(task);
    cout << "Added Task: " << task << " to the back of the queue.\n";
}

void addFrontToQueue(deque<string> &tms, string task)
{
    tms.push_front(task);
    cout << "Added Task: " << task << " to the front of the queue.\n";
}

void processTask(deque<string> &tms)
{
    cout << "Processing Task: " << tms.front() << "\n";
    tms.pop_front();
}

void displayQueue(deque<string> &tms)
{
    cout << "Current Queue: \n";
    deque<string> temp;
    temp = tms;
    int i = 1;
    while (!temp.empty())
    {
        cout << i << ". " << temp.front() << "\n";
        temp.pop_front();
        i++;
    }
}

int main()
{
    deque<string> tms;
    // Add task to back fo queue
    addBackToQueue(tms, "Task 1");

    // addd task to front of queue
    addFrontToQueue(tms, "Urgent Task");

    //add task to back of queue
    addBackToQueue(tms, "Task 2");

    // process task
    processTask(tms);

    // display current queue
    displayQueue(tms);

    return 0;
}