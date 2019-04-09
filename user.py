# import pyperclip
class User:
  """
  Class that generates new instances of users
  """ 
  details_list = []
  def __init__(first_name, last_name, phone_number, email, password):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email
    self.password = password
  def save_user(self):
    '''
    Saves new user details into details_list
    '''
    User.details_list.append(self)
​
  def delete_user(self):
    '''
    Deletes user profile from details_list
    '''
    User.details_list.remove(self)
  @classmethod
  def user_exist(dls, number):
     '''
    Method that checks if a user profile exists from the contact list.
    Args:
      number: Phone number to search if it exists
    Returns :
      Boolean: True or false depending if the user exists
    '''
​
     for user in dls.details_list:
      if user.phone_number == number:
          return True
​
          return False
  @classmethod
  def display_users(dls):
    '''
    method that returns the users details list
    '''
    return dls.details_list
​