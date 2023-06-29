class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.leftChild = None 
      self.rightChild = None 
      self.height = 0
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None
    #should there be another field that tracks total height of the tree 
    # TODO complete initialization

  #the rotate left method runs in constant time, because through the rightchild/leftchild reference the method has immediate access to all nodes that are needed for rotate, it also calls the node height calc mathod with runs in constant time
  def __rotateLeft(self, currentNode):
      newRoot = currentNode.rightChild
      newLeft = currentNode
      floater = newRoot.leftChild
      newRoot.leftChild = newLeft
      currentNode.rightChild = floater
      self.nodeHeightCalc(currentNode)
      self.nodeHeightCalc(newRoot)
      return newRoot #returns the new root(the old roots left child) as the new root of the subtree 
  
  #the rotate right method runs in constant time, because through the leftchild/rightchild reference the method has immediate access to all nodes necesary to rotate the subtree right, it also calls the node height calc mathod with runs in constant time
  def __rotateRight(self, currentNode):
      newRoot = currentNode.leftChild
      newRight = currentNode
      floater = newRoot.rightChild 
      newRoot.rightChild = newRight  #sets the new root's right child to the old root 
      currentNode.leftChild = floater # sets the old roots left child to the floater
      self.nodeHeightCalc(currentNode)
      self.nodeHeightCalc(newRoot)
      return newRoot #returns the new root(the old roots left child) as the new root of the subtree 
  
  #the get node balance method runs in constant time as the balance of the node is just a function of the nodes height which is stored as an attribute
  def __getNodeBalance(self, currentNode):
    if currentNode.rightChild == None and currentNode.leftChild == None:
      return 0
    elif currentNode.rightChild != None and currentNode.leftChild == None:
      return currentNode.rightChild.height
    elif currentNode.rightChild == None and currentNode.leftChild != None:
      return (0 - currentNode.leftChild.height)
    else:
      return (currentNode.rightChild.height - currentNode.leftChild.height)

  #the balance method runs in constant time as it uses the rotateleft,rotateright and getNodeBalance method to decide whether and how to rotate a subtree. All those methods used are constant time opperations so balance is runs in constant time
  def __balance(self, currentNode):
    # error throwing because it is trying to balance a node with object none, why is this happening
    currentNodeBalance = self.__getNodeBalance(currentNode)
    if currentNodeBalance == 0 or currentNodeBalance == 1 or currentNodeBalance == -1: #if the balance is zero return currentNode, the subtree is already balanced 
      return currentNode
    if currentNodeBalance == -2: #if the balance of currentNode is -2, meaning the binary tree is left heavy, check the balance of currentNode's left child 
      currentNodeLeftChildBalance = self.__getNodeBalance(currentNode.leftChild)
      if currentNodeLeftChildBalance == -1 or currentNodeLeftChildBalance == 0: # if the balance of currentNode's left child is -1 or 0, then rotate the tree rooted at currentNode to the right about currentNode
        return self.__rotateRight(currentNode)
      if currentNodeLeftChildBalance == 1: #if the balance of the currentNode's left child is 1, then a double rotation is needed, so first rotate the subtree rooted at the currentNode's left child left about the currentNode's left child (into the imbalance) and then rotate the subtree rooted at the currentNode right about the current Node
        currentNode.leftChild = self.__rotateLeft(currentNode.leftChild)  # this will be a left rotation about currentNodes left child into the imbalance
        return self.__rotateRight(currentNode)
    if currentNodeBalance == 2: #if the balance of the currentNode is +2, meaning the binary tree is right heavy, check the balance of currentNode's right child
      currentNodeRightChildBalance = self.__getNodeBalance(currentNode.rightChild)
      if currentNodeRightChildBalance == 1 or currentNodeRightChildBalance == 0: #if the balanace of currentNode's right child is 1 or 0, rotate the subtree rooted at currentNode to the left about the currentNode 
        return self.__rotateLeft(currentNode)
      if currentNodeRightChildBalance == -1: #if the balance of the currrent Node's right child is -1, then a double rotation is needed, so first rotate the subtree rooted at the currentNode's right child right about the currentNode's right child (into the imbalance) and then rotate the subtree rooted at the currentNode left about the current Node
        currentNode.rightChild = self.__rotateRight(currentNode.rightChild) # this will be a right rotation about currentNode's right child into the imbalance 
        return self.__rotateLeft(currentNode)  

    

    #takes a node as a parameter and treats it as the root of a subtree 
    #If the subtree is unbalanced it rotates it 
    #Works in constant time 
    # to detect imbalance subtract the height of the left child subtree from the height of the right child subtree
    # make sure to flag if its right heavy or left heavy (if its +2 or -2)
    #if it is heavy by 2 check the imbalance of the heavy child 
    #if the signs are different (+2 and -1 for example) rotate once towards the imbalance and once away from the imbalance 

  # the nodeHeightCalc method runs in constant time as it uses the height attirbute stored for the the two child nodes of the current node to calculate the current nodes height
  def nodeHeightCalc(self, currentNode):
    if currentNode == None:
      currentNode.height = 0
    if currentNode.leftChild == None and currentNode.rightChild == None: 
      currentNode.height = 1
    elif currentNode.rightChild == None and currentNode.leftChild != None:
      currentNode.height = 1 + currentNode.leftChild.height
    elif currentNode.rightChild != None and currentNode.leftChild == None:
      currentNode.height = 1 + currentNode.rightChild.height
    else:
      currentNode.height = max(currentNode.rightChild.height, currentNode.leftChild.height) + 1

  #the rec_insert method runs in 0(log n) time because the AVL tree always makes sure the number of nodes is an exponential function of the height and thus traversing the tree to add nodes will be a logarithmic function
  #in addition the balance method that is called in the remove element runs in constant time so that has no effect on rec_removes run time 
  def rec_insert(self, currentNode, numberToInsert):
    if currentNode == None: 
      nodeToInsert = self.__BST_Node(numberToInsert)
      nodeToInsert.height = 1
      return nodeToInsert
    else:
      if numberToInsert < currentNode.value:
        currentNode.leftChild = self.rec_insert(currentNode.leftChild, numberToInsert)
      if numberToInsert > currentNode.value:
        currentNode.rightChild = self.rec_insert(currentNode.rightChild, numberToInsert)
      if numberToInsert == currentNode.value:
        raise ValueError
      

      self.nodeHeightCalc(currentNode)
  
      return self.__balance(currentNode) #change to return self.__balance(currentNode)


  #An important consideration here is that a non-existent subtree has height 0 (be careful not to crash in this case). 
  #Also notice that the heightof the subtree rooted at a newly created node object is always 1.
  #update height before returning (height of largest subtree plus one)

  #since the insert_element function calls rec_insert it runs in o(log n) time because the AVL tree always makes sure the number of nodes is an exponential function of the height and thus traversing the tree to add nodes will be a logarithmic function
  def insert_element(self, value):
     self.__root = self.rec_insert(self.__root, value)

  #rec_remeove_element runs in O(log n) times because because the AVL tree always makes sure the number of nodes is an exponential function of the height and thus traversing the tree to remove nodes will be a logarithmic function
  #in addition the balance method that is called in the remove element runs in constant time so that has no effect on rec_removes run time 
  def rec_remove_element(self, currentNode, numberToRemove):
    #how to delete values
    #if value is not found raise error 
    if currentNode == None:
      raise ValueError
    if currentNode.value > numberToRemove: #if the value we are looking for is less than the current node value we recur on the left child
      currentNode.leftChild = self.rec_remove_element(currentNode.leftChild, numberToRemove)
      #self.nodeHeightCalc(currentNode)
    elif currentNode.value < numberToRemove: #if the value we are looking for is greater than the current node value we recur on the right child
      currentNode.rightChild = self.rec_remove_element(currentNode.rightChild, numberToRemove)
      #self.nodeHeightCalc(currentNode)
    else: #if the current node value is equivalent to the number we want to remove 
      if currentNode.rightChild == None: #if right child is none return the left child
        #print('case 1')
        return currentNode.leftChild #if both are none itll return the left child which is already none :)
      if currentNode.leftChild == None: #if the left child is none renturn the right child
        #print('case 2')
        return currentNode.rightChild
      #print('case 3')
      minNode = currentNode.rightChild #if both are none, find the smallest nodevalue on the tree stemming from the currentNodes right child
      while minNode.leftChild != None:
        minNode = minNode.leftChild 
      currentNode.value = minNode.value #swap the value of the smallest to the current node
      currentNode.rightChild = self.rec_remove_element(currentNode.rightChild, minNode.value) #delete the smallest node starting at current.rightChild which is trivial since it is a leaf node and assign a new right child
      #this isnt working (hmm)
      
    self.nodeHeightCalc(currentNode)

    
    return self.__balance(currentNode) 

  #this runs in O(logn) time because it calls the rec_remove method 
  def remove_element(self, value):
    self.__root = self.rec_remove_element(self.__root, value)

  #the rec_in_order method runs in o(n) time since the method vistis everynode and creates a string representation of the inorder traversal of the tree 
  def rec_in_order(self, currentNode):
    if currentNode == None:
      return ''
    else:
      inOrderString = str(self.rec_in_order(currentNode.leftChild)) + str(currentNode.value) + ', ' + str(self.rec_in_order(currentNode.rightChild))
      return inOrderString

  #this method runs in o(n) time as it calls the rec_in_order method and simply applies constant time adjustments to the string returned by rec_in_order to achieve the proper format 
  def in_order(self):
    if self.__root == None:
      return '[ ]'
    currentNode = self.__root 
    unformattedString = self.rec_in_order(currentNode)
    formattedString = unformattedString[0:len(unformattedString) - 2]#string problem originates here adds the commas between numbers 
    return f"[ {formattedString} ]"
    #add the dot joins here i guess and the brackets that enlcose the str format 

  #the rec_pre_order method runs in o(n) time since the method vistis everynode and creates a string representation of the preorder traversal of the tree 
  def rec_pre_order(self, currentNode):
    if currentNode == None:
      return ''
    else:
      preOrderString = str(currentNode.value) + ', ' + str(self.rec_pre_order(currentNode.leftChild)) + str(self.rec_pre_order(currentNode.rightChild))
      return preOrderString  

  #this method runs in o(n) time as it calls the rec_pre_order method and simply applies constant time adjustments to the string returned by rec_pre_order to achieve the proper format 
  def pre_order(self):
    if self.__root == None:
      return '[ ]'
    currentNode = self.__root 
    unformattedString = self.rec_pre_order(currentNode)
    formattedString = unformattedString[0:len(unformattedString) - 2]
    return f"[ {formattedString} ]"

  #the rec_post_order method runs in o(n) time since the method vistis everynode and creates a string representation of the postorder traversal of the tree 
  def rec_post_order(self, currentNode):
    if currentNode == None:
      return ''
    else:
      postOrderString = str(self.rec_post_order(currentNode.leftChild)) + str(self.rec_post_order(currentNode.rightChild)) + str(currentNode.value) + ', '
      return postOrderString  

  #this method runs in o(n) time as it calls the rec_post_order method and simply applies constant time adjustments to the string returned by rec_post_order to achieve the proper format 
  def post_order(self):
    if self.__root == None:
      return '[ ]'
    currentNode = self.__root 
    unformattedString = self.rec_post_order(currentNode)
    formatedString = unformattedString[0:len(unformattedString) - 2]
    return f"[ {formatedString} ]"


  #the rec_to_list method runs in o(n) time as it visits every node in the tree in the inorder traversal format and concatinates each node to a list as it goes 
  def rec_to_list(self, currentNode, inOrderList):
    if currentNode == None:
      return 
    if currentNode.leftChild != None:
      self.rec_to_list(currentNode.leftChild, inOrderList)
    inOrderList.append(currentNode.value)
    if currentNode.rightChild != None:
      self.rec_to_list(currentNode.rightChild, inOrderList)

  #the to list method runs in o(n) time as it calss the rec_to_list method
  def to_list(self):
    currentNode = self.__root 
    inOrderList = []
    self.rec_to_list(currentNode, inOrderList)
    return inOrderList

  #the get_height method runs in constant time as the height of one node is 1 + the absolute value of the node's longest child(this is all computed constantly by the nodeHeightCalc method above)
  def get_height(self):
    if self.__root == None:
      return 0
    return self.__root.height

  #the str method runs in o(n) time as it simply calls the in_order fucntion above
  def __str__(self):
    return self.in_order()

# if __name__ == '__main__':
#   a = Binary_Search_Tree() #possibly has to be BST Node 
#   a.insert_element(30)
#   a.insert_element(20)
#   a.insert_element(10)
#   a.insert_element(5)
#   print('before removal')
#   print(a.in_order())
#   a.remove_element(5)
#   # a.insert_element(6)
#   # a.insert_element(1)
#   print('after removal')
#   print(a.in_order())
#   #print(a.pre_order())
#   #print(a.post_order())
#   #print(a.get_height())
#   # print("this is to list")
#   # print(a.to_list())
#   # print("height before removal")
#   # print(a.get_height())
#   # a.remove_element(1)
#   # #print("after removal 1")
#   # print(a.in_order())
#   # print("height after removal")
#   # print(a.get_height())
#   # #a.remove_element(2)
#   # #print("after removal 2")
#   # #print(a.in_order())

#   #pass #unit tests make the main section unnecessary.

