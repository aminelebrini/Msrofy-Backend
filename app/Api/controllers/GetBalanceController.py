from services.GetBalanceService import GetBalanceService

class GetBalanceController:
    def __init__(self, db):
        self.db = db
        self.get_balance_service = GetBalanceService(db)

    def get_balance(self,Group: int):

        balance = self.get_balance_service.get_balance(Group)

        if(balance is None):
            return {
                "message": "No balance found for the given group."
            }
        return {
            "message": "Balance retrieved successfully.",
            "balance": balance
        }