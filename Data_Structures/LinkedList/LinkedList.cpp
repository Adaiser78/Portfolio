#include "LinkedList.h"
#include <iostream>




Node::Node() {
	
	data = "";
	next = nullptr;
	prev = nullptr;

}
Node::Node(string data) {

	this->data = data;
	next = nullptr;
	prev = nullptr;

}
Node::Node(string data, Node* next, Node* prev) {

	this->data = data;
	this->next = next;
	this->prev = prev;

}


LinkedList::LinkedList() {

	this->head = nullptr;
	this->tail = nullptr;

}

LinkedList::~LinkedList() {

	Node* tmp = head;

	while (tmp != nullptr) { // We're doing tmp because we will reach a point where tmp doesn't have a next.
		
		head = head->next;

		delete tmp;

		tmp = head;
	}
	tail = nullptr;
}

LinkedList::LinkedList(const LinkedList& ll) {

	if (ll.head == nullptr) {
		head = nullptr;
	}
	else {
		// Copy the first node
		head = new Node(ll.head->data);
		Node* current = head;
		Node* otherCurrent = ll.head->next;

		// Copy the rest of the nodes
		while (otherCurrent != nullptr) {
			current->next = new Node(otherCurrent->data);
			current = current->next;
			otherCurrent = otherCurrent->next;
		}
	}
}


void LinkedList::append(string data) {

	Node *tmp = new Node(data);

	tmp->prev = tail;

	if (head == nullptr) {

		head = tmp;	
	}
	else {

		tail->next = tmp;
	}

	tail = tmp; // You're setting the tail to tmp no matter what. 


}

void LinkedList::prepend(string data) {

	Node* tmp = new Node(data);

	tmp->next = head;

	if (head == nullptr) {

		tail = tmp;
	}
	else {
		
		head->prev = tmp;
	}
	
	
	head = tmp; // You're setting the head to tmp and tmp-next to head. 

}

bool LinkedList::search(string data) {

	Node* tmp = head;

	while (tmp != nullptr) { // We're doing tmp because we will reach a point where tmp doesn't have a next.
		if (tmp->data == data) { // Check if the Node data is the value we're looking for. 
			return true; // Return true if found.
		}
		else {
			tmp = tmp->next; // Set tmp to point to the next node, or nullptr if last. 
		}
	}

	return false; // Return false if not found. 

}

bool LinkedList::remove(string data) {

	Node* tmp = head;
	

	while (tmp != nullptr) { // Until we reach the last node.

		if (tmp->data == data) { // If the node's data matches what we're looking for. 

			if (tmp->prev != nullptr) {
				tmp->prev->next = tmp->next;
			}

			if (tmp->next != nullptr) {

				tmp->next->prev = tmp->prev;
			}

			if (tmp == head) {
				head = tmp->next; // In the case of it being the first node, we must change head.
			}
			
			if (tmp == tail) { // In the case of it being the last node, we must change the tail. 
				tail = tmp->prev;
			}


			delete tmp; 
			return true;
			
		}

		
		tmp = tmp->next;


	}
	return false;

}

void LinkedList::display() {

	Node* tmp = head;

	while (tmp != nullptr) { // We're doing tmp because we will reach a point where tmp doesn't have a next.
		
		std::cout << tmp->data << " ";

		tmp = tmp->next;
	}

	std::cout << endl;

	 // Return false if not found. 

}

void LinkedList::tailDisplay() {

	Node* tmp = tail;

	while (tmp != nullptr) { // We're doing tmp because we will reach a point where tmp doesn't have a next.

		std::cout << tmp->data << " ";

		tmp = tmp->prev;
	}

	std::cout << endl;

	// Return false if not found.


}

bool LinkedList::tailRemove(string data) {

	if (this->remove(data)) {
		return true;
	};

	return false;
	

	
}

