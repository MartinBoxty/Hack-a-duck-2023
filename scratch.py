import json
import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYmYiOjE2OTYwMzIwMDAsImFwaV9zdWIiOiI4MzE4NTZlZWViMjQ5MGI0N2Q4NWUzZjM4MTBjNjczZWY1YjgxZmIwMjQ2NTQ0NGVlMzIyNWM3ZDUwN2NjNjU0MTcxNzIwMDAwMDAwMCIsInBsYyI6IjVkY2VjNzRhZTk3NzAxMGUwM2FkNjQ5NSIsImV4cCI6MTcxNzIwMDAwMCwiZGV2ZWxvcGVyX2lkIjoiODMxODU2ZWVlYjI0OTBiNDdkODVlM2YzODEwYzY3M2VmNWI4MWZiMDI0NjU0NDRlZTMyMjVjN2Q1MDdjYzY1NCJ9.NXDkICmn8y_BMVFD_FAF1pXm8B9hq5wq4eJYk_4X2ozaKeNpr7-x1M1NL515Iqf-Zbvq9j5aWgS7G2eK_O5rTeF8TsTI9xTdxkrDrV3ALnP3KioCnBdyW5QtAzof7C-GrHjrpjui4VM-nQ4NUgXL9S7jD3Nz2oyc9BYes6eZQJ0oIYiCou_T8_ecKHjSuF7i4OCmfaqwDs6MqkIxt_ZIU8q43Db3Cy3rWz_P1L82Sf03T0das8be9BmYGWjwCdMHt4oBcqj7RVg9ixxC58KAmLfsmqJ60gMSqr47x-yW2vNJLshmmlL__N-oW4-xzOkwxl0qE5cXNhxoLRInrwG26w"

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'version': '1.0'
}

quantity = 2
numTransactions = 6
liveBalance = False

payload = json.dumps({"quantity": quantity, "numTransactions": numTransactions, "liveBalance": liveBalance})


response = requests.post("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/create", headers=headers, data=payload).text
json_response = json.loads(response)
