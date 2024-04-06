import FormsAPI
import time
print("id")
d = input()
print(FormsAPI.FormsResp.GetResp(d))
time.sleep(2)
print(FormsAPI.FormsResp.GetForm(d))
