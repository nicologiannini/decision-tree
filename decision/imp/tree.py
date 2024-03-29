from decision.imp._node import Node, next_leaf

class DecisionTree:
    """
    DecisionTree uses the gini index to create decision points for classification tasks.
    The goal is to create a model capable of predicting a target variable, building the decision
    rules by learning from the data.

    """
    def __init__(self):
        #indicates whether the tree is fully built or not
        self.finished = False
        #the root is the node from which the branches will start
        self.root = None
    def build(self, header, content, target):
        """
        Develops the decision tree based on the data.

        """
        #for now it branches out as much as possible
        #TODO add a parameter that allows you to specify the maximum depth of the tree
        while self.finished == False:
            if self.root:
                self.finished = True
            else:
                next_node = next_leaf(header, content, target)
                self.root = Node(header, content, target, next_node[1], next_node[0])
    
    def predict(self, header, content):
        """
        Processes the predicted target variable based on the tree

        """
        prediction = []
        for item in content:
            predict = self.check_node(header, self.root, item)
            prediction.append(predict)
        return prediction
    
    def check_node(self, header, node, item):
        """
        Iterative logic to check the condition of each node, until the path is exhausted
        and the variable is predicted

        """
        if node.res == None:
            if node.f_value == item[header.index(node.field)]:
                res = self.check_node(header, node.left, item)
                return res
            else:
                res = self.check_node(header, node.right, item)
                return res
        else:
            return node.res