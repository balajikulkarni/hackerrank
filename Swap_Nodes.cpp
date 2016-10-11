#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void swaper(int** Tree,int node,int depth_needed,int current_depth){
     
    if(node == -1)
        return;
    
    if(current_depth % depth_needed == 0)
    {
        int temp = Tree[node][0];
        Tree[node][0]= Tree[node][1];
        Tree[node][1]= temp;
    }
     
    swaper(Tree,Tree[node][0],depth_needed,current_depth+1);
    cout << node <<" ";
    swaper(Tree,Tree[node][1],depth_needed,current_depth+1);
    
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int N,T,depth;
    
    cin >> N;
    
    int** Tree = new int*[N+1];
   
    for(int i=0;i<N+1;i++){
        Tree[i]=new int[2];
        
    }
          
    for(int i=1;i<N+1;i++){
        for(int j=0;j<2;j++){
            cin >> Tree[i][j]; 
           
        }
    }
    
    cin >> T;
    
    for(int i=0;i<T;i++){
        cin >> depth;
        swaper(Tree,1,depth,1);
        cout <<"\n";
    }
    
    for(int i=0;i<N+1;++i)
        delete [] Tree[i];
    delete [] Tree;
    
    return 0;
}

