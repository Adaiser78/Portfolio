#pragma once

#include <string>
using namespace std;

class Node 
{

public:

	string data;
	Node* next;
	Node* prev;

	Node();
	Node(string data);
	Node(string data, Node* next, Node* prev);

};




class LinkedList 
{

private:
	Node *head, *tail;

public:
	LinkedList();
	~LinkedList();
	LinkedList(const LinkedList& ll);

	void append(string data);
	void prepend(string data);
	bool search(string data);
	bool remove(string data);
	bool tailRemove(string data);
	void tailDisplay();
	void display();


};

