import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount ):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = datetime.utcnow().isoformat()

    def update(self, title = None, amount = None):
            if title is not None:
              self.title = title
            if amount is not None:
              self.amount = amount
       
            self.updated_at = datetime.utcnow()
            return f"Expense was updated successfully at {self.updated_at}"
        
        
    def to_dict(self):
            return{
                "id" : self.id,
                "title" : self.title,
                "amount" : self.amount,
                "created_at" : self.created_at,
                "updated_at" : self.updated_at
            }  
    
    def __repr__(self) -> str:
            return f"{self.title}_{self.amount}"
    
        

# ExpenseDatabase

class ExpenseDatabase:
    def __init__(self):

        self.expense = []

    def add_expense(self, expense):
        self.expense.append(expense)
        print(f"{expense} was added successfully!")

    def remove_expense(self, expense_id):
        self.expense = [expense for expense in self.expense if expense_id != expense_id]
        print(f"expense with id {expense_id} has been remove successfully!")

    def get_expense_by_id(self, expense_id):

        expense = [expense for expense in self.expense if expense_id == expense.id]
        if len(expense) == 0:
            return None
        return expense[0].to_dict()
    
    def get_expense_by_title(self, expense_title):
       return [expense.to_dict() for expense in self.expense if expense.title == expense_title ]
   
        
    def to_dict(self):
        return [expense.to_dict for expense in self.expense]
        
    
    
if __name__ == "__main__" :
    
    expense_1 = Expense (title = 'Transportation', amount= 15000)
    expense_2 = Expense (title ='Food', amount= 30000)
    expense_3 = Expense (title= "Misc", amount= 10000) 
                   

    edb = ExpenseDatabase() 

    for expense in [expense_1, expense_2, expense_3]:
        edb.add_expense(expense)
        print(edb.expense)
        print()
        print("#" * 20)
        print()       
    
    print(edb.get_expense_by_id(expense_1.id, ))
