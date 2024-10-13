#pragma once

class Node
{

public:

	int data;
	Node* left;
	Node* right;

	Node();
	Node(int data);
	int const degree();
	

};

class BST {


private: 
	Node* root;
	bool search(Node* node, int data);
	bool insert(Node*& node, int data);
	bool remove(Node*& node, int data);
	void postOrder(Node* node);

public:

	

	BST();
	bool Search(int data);
	bool Insert(int data);
	bool Remove(int data);
	void PostOrder();



};