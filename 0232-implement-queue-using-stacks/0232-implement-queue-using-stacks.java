class MyQueue {
    Stack<Integer> s=new Stack<>();

    public MyQueue(){

    }
    
    public void push(int x) {
        if(s.isEmpty()){
            s.push(x);
        }else{
            int top=s.pop();
            push(x);
            s.push(top);
        }
    }
    
    public int pop() {
        return s.pop();
    }
    
    public int peek() {
        return s.peek();
    }
    
    public boolean empty() {
        return s.isEmpty();
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */

class MyStack {

    Queue<Integer> q;

    public MyStack() {
        q=new LinkedList<>();
    }
    
    public void push(int x) {
        q.add(x);
        for(int i=1;i<q.size();i++){
            q.add(q.remove());
        }
    }
    
    public int pop() {
        return q.remove();
    }
    
    public int top() {
        return q.peek();
        
    }
    
    public boolean empty() {
        return q.isEmpty();
    }
}