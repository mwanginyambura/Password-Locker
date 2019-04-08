import pyperclip
class Credential:

   """
   Class that generates new instances of credentials.
   """
   Credential_list = []

   def __init__(self,view_password ,account,logic,password):
       self.view_password = view_password
       self.account = account
       self.login = login
       self.password = password


   credential_list = []
   def save_credentials(self):
       '''
       save_credentials method saves credentials objects into credentials_list
       '''
       credentials.credentials_list.append(self)

   @classmethod
   def display_credentials(cls):
       '''
       method that returns the credential list
       '''
       return cls.credentials_list
   def delete_credentials(self):

       '''
       delete_credentials method deletes a saved credentials from the credentials_list
       '''

       credentials.credentials_list.remove(self)
   @classmethod
   def copy_password(cls,number):
       credentials_found = Credential.find_by_number(number)
       pyperclip.copy(credentials_found.password)