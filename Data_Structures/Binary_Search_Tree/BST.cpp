#include "BST.h"
#include <iostream>

Node::Node() {

	data = 0;
	left = nullptr;
	right = nullptr;

}
Node::Node(int data) {

	this->data = data;
	left = nullptr;
	right = nullptr; 

}

int const Node::degree() {
	int degree = 0;
	if (this->left != nullptr) {
		degree += 1;
	}
	if (this->right != nullptr) {
		degree += 1;
	}
	return degree;

}

BST::BST() {

	this->root = nullptr;
}

bool BST::search(Node* node, int data) {

	if (node == nullptr) {
		return false;
	}

	else if (data < node->data) {
		return this->search(node->left, data);
	}

	else if (data > node->data) {
		return this->search(node->right, data);
	}

	else {
		return true;
	}
}

bool BST::Search(int data) {

	return this->search(this->root, data);

}

bool BST::insert(Node *&node, int data) {

	if (node == nullptr) {
		node = new Node(data);
		return true;
	}
	else if (data < node->data){
		return this->insert(node->left, data);
	}
	else if (data > node->data) {
		return this->insert(node->right, data);
	}

	
	return false;

}

bool BST::Insert(int data) {
	return this->insert(this->root, data);
}

bool BST::remove(Node*& node, int data) {

	if (node == nullptr) {
		return false;
	}
	else if (data > node->data) {
		return this->remove(node->right, data);
	}
	else if (data < node->data) {
		return this->remove(node->left, data);
	}

	else {
		if (node->degree() == 0) {
			delete node;
			node = nullptr;
		}
		else if (node->degree() == 1) {
			Node* tmp = node;
			if (node->left != nullptr) {
				node = node->left;
			}
			else {
				node = node->right;
			}
			delete tmp;
		}
		else {
			Node* tmp = node;
			while (tmp->right != nullptr) {
				tmp = tmp->right;
			}
			node->data = tmp->data;
			this->Remove(tmp->data);
		}
		return true;
	}

}

bool BST::Remove(int data) {
	return this->remove(this->root, data);
}

void BST::postOrder(Node* node) {
	int count = 0;
	if (node == nullptr) { return; };
	this->postOrder(node->left);
	this->postOrder(node->right);
	if (node->data == this->root->data) {
		count += 1;
	}
	if ((node->data != this->root->data) || count != 2) {
		std::cout << node->data << " ";
	}


}

void BST::PostOrder() {
	this->postOrder(this->root);
}
