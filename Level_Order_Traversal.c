Algo Description:
1. Compute the height of the tree as below:
	if root is Null , return 0;
	else leftheight = height(root->left);
	     rightheight = height(root->right);
         if (leftheight> rightheight)
			 leftheight+1
		 else
			 rightheight+1
		 
2. For each level < height 
	  Call  GivenLevel
	  
3. In GivenLevel	  
		if the level is 1 means we are at required node ,hence print it
		else recursively do the following
			GivenLevel(root->left,level-1)
		    GivenLevel(root->right,level-1)

/*
struct node
{
    int data;
    node* left;
    node* right;
}*/

int height(node *root)
{
    int l,r;
    
    if(root == NULL)
        return 0;
    else{
       l= height(root->left);
       r= height(root->right);
        
        if(l>r)
           return(l+1);
        else
           return(r+1);
    }
     
}

void GivenLevel(node *root,int level)
{
    if(root==NULL)
       return;
    
    if(level == 1)
       printf("%d ",root->data);
    else if(level > 1)
    {
        GivenLevel(root->left,level-1);
        GivenLevel(root->right,level-1);
    }
    
}


void LevelOrder(node * root)
{
    if (root== NULL)
        return;
    
    int h = height(root);
    int i;
       
    for(i=1;i<=h;i++)
        GivenLevel(root,i);
    
}
