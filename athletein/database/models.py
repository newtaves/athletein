from firebase_admin.firestore import FieldFilter

class User:
    def __init__(self, db):  # Pass the Firestore client to the class
        self.db = db

    def add_user(self, name='test', password='test', email='alice@gmail.com'):
        try:
            docs = self.db.collection("users").where(filter=FieldFilter("email", "==", email)).get()
            if not docs:  # More Pythonic way to check if the list is empty
                doc_ref = self.db.collection("users").document()  # Let Firestore generate the ID
                doc_ref.set({
                    "name": name,
                    "email": email,
                    "password": password  # In a real app, *never* store passwords in plain text!
                })
                return {'status': 'success', 'message': 'User created!!', 'user_id': doc_ref.id} # Return the ID
            else:
                return {'status': 'error', 'message': 'Email already Exists!!'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}  # Convert exception to string

    def check_password(self, email, password):
        try:
            docs = self.db.collection("users").where(filter=FieldFilter('email', '==', email)).get()
            if docs:
                doc = docs[0]  # Get the first document (assuming email is unique)
                stored_password = doc.to_dict().get('password')
                if stored_password == password:  # change to Hash in production
                    return {'status': 'success', 'message': 'Password matched!', 'user_id': doc.id}
                else:
                    return {'status': 'error', 'message': 'Incorrect password!'}
            else:
                return {'status': 'error', 'message': 'User not found!'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def get_user_by_id(self, user_id):
        try:
            doc_ref = self.db.collection("users").document(user_id)
            doc = doc_ref.get()
            if doc.exists:
                return {'status': 'success', 'user_data': doc.to_dict()}
            else:
                return {'status': 'error', 'message': 'User not found'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}