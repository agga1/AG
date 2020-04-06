#include <list>
#include <iostream>
#include <queue>
#include <limits>
#include <algorithm>
#include <unordered_map>

using namespace std;
#define NIL 0
#define INF INT32_MAX

class Graph
{
    int m, n;
    list<int> *adj;

    int *pairL, *pairR, *dist;

public:
    explicit Graph(int V){
        this->m = V;
        this->n = V;
        adj = new list<int>[m+1];
        pairL = new int[m+1];
        pairR = new int[n+1];
        dist = new int[m+1];
    }
    void addEdge(int u, int v); // To add edge
    void removeEdge(int u, int v); // To add edge

    bool bfs(); // check for existence of aug path
    bool dfs(int u);

    int hopcroftKarp(); // ret max matching size
    void printPairs();
};
void Graph::printPairs() {
    for(int i=1;i<=m;i++){
        if(pairL!=NIL)
            cout<<i<<" "<<pairL[i]<<endl;
    }
};
int Graph::hopcroftKarp()
{
    for (int u=0; u<=m; u++)
        pairL[u] = NIL;
    for (int v=0; v<=n; v++)
        pairR[v] = NIL;

    int matchingSize = 0;

    while (bfs()) {
        for (int u=1; u<=m; u++)
            if (pairL[u]==NIL && dfs(u))
                matchingSize++;
    }
    return matchingSize;
}

bool Graph::bfs()
{
    queue<int> toProcess;

    for (int u=1; u<=m; u++) {
        if (pairL[u]==NIL) {
            dist[u] = 0;
            toProcess.push(u);
        }
        else dist[u] = INF;
    }

    dist[NIL] = INF;

    while (!toProcess.empty())
    {
        int u = toProcess.front();
        toProcess.pop();

        if (dist[u] < dist[NIL]) {
            for (auto v: adj[u]) {
                if (dist[pairR[v]] == INF) {
                    dist[pairR[v]] = dist[u] + 1;
                    toProcess.push(pairR[v]);
                }
            }
        }
    }
    return (dist[NIL] != INF);
}

bool Graph::dfs(int u)
{
    if (u != NIL)
    {
        list<int>::iterator i;
        for (auto v: adj[u]) {
            if (dist[pairR[v]] == dist[u]+1) {
                if (dfs(pairR[v])) {
                    pairR[v] = u;
                    pairL[u] = v;
                    return true;
                }
            }
        }

        dist[u] = INF;
        return false;
    }
    return true;
}

void Graph::addEdge(int u, int v)
{
    adj[u].push_back(v);
}
void Graph::removeEdge(int u, int v)
{
    adj[u].remove(v);
}
struct Event{
    int value;
    int from, to;
    bool start;
    Event(int value, int from, int to, bool start){
        this->value = value;
        this->from = from;
        this->to = to;
        this->start = start;
    }
    Event(){
        this->value = 0;
        this->from = 0;
        this->to = 0;
        this->start = false;
    }
};
int main()
{
    int testCases, V, E;
    cin>>testCases;
    for(int i=0;i<testCases;i++) {
        bool found = false;
        int activeE = 0;
        cin>>V>>E;
        vector<Event> events;
        Graph g(V);
        for (int j = 0; j < E; j++) {
            int from, to, l, u;
            cin >> from >> to >> l >> u;
            events.push_back(Event(l, from, to, true));
            events.push_back(Event(u+1, from, to, false)); // ends closed
        }
        sort(begin(events), end(events), [](Event a, Event b) {return a.value < b.value; }); // asc!!
        int it=0;
        while(it < events.size()){
            vector<Event> currEvents;
            currEvents.push_back(events[it]);
            // find all events w same value
            while(it+1 <events.size() && events[it].value == events[it+1].value){
                it++;
                currEvents.push_back(events[it]);
            }
            for(auto e:currEvents){
                if(e.start){
                    g.addEdge(e.from, e.to);
                    activeE++;
                }else{
                    g.removeEdge(e.from, e.to);
                    activeE--;
                }
            }
            if(activeE>= V && g.hopcroftKarp() == V){ // max matching is perfect, we found the answer
                cout<<currEvents[0].value<<endl;
                g.printPairs();
                found=true;
                break;
            }
            it++;
        }
        if(!found)
            cout<<-1<<endl;
    }

    return 0;
}
