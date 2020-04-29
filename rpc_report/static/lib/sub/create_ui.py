from odoolib import get_connection
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

con = get_connection(hostname='next.odoo.com', protocol='xmlrpcs', port=443, database='openerp', login='tfr', password='chevalbleu', user_id=104)
partner = con.get_model('res.partner')
print(partner.search([], limit=20))
po = con.get_model('pos.order')
context = {"lang":"en_US","tz":"CET","uid":104,"allowed_company_ids":[1]}
data = {
     "name":"Order 00126-003-0008",
     "amount_paid":227.71,
     "amount_total":227.71,
     "amount_tax":39.52,
     "amount_return":0,
     "lines":[
         [0,0,{"qty":1,"price_unit":100,"price_subtotal":100,"price_subtotal_incl":121,"discount":0,"product_id":11808,"tax_ids":[[6,False,[5]]],"pack_lot_ids":[],"note":""}],
         [0,0,{"qty":1,"price_unit":20.66,"price_subtotal":20.66,"price_subtotal_incl":25,"discount":0,"product_id":334,"tax_ids":[[6,False,[1884]]],"pack_lot_ids":[],"note":""}],
         [0,0,{"qty":1,"price_unit":16.53,"price_subtotal":16.53,"price_subtotal_incl":20,"discount":0,"product_id":335,"tax_ids":[[6,False,[1884]]],"pack_lot_ids":[],"note":""}],
         [0,0,{"qty":1,"price_unit":23,"price_subtotal":23,"price_subtotal_incl":27.83,"discount":0,"product_id":12511,"tax_ids":[[6,False,[5]]],"pack_lot_ids":[],"note":""}],
         [0,0,{"qty":1,"price_unit":28,"price_subtotal":28,"price_subtotal_incl":33.88,"discount":0,"product_id":11414,"tax_ids":[[6,False,[5]]],"pack_lot_ids":[],"note":""}]],
    "statement_ids":[[0,0,{"name":"2020-02-10 10:22:08","payment_method_id":4,"amount":227.71,"payment_status":"","ticket":"","card_type":"","transaction_id":""}]],
    "pos_session_id":126,
    "pricelist_id":66,
    "partner_id":False,
    "user_id":104,
    "employee_id":False,
    "uid":"00126-003-0006",
    "sequence_number":8,
    "fiscal_position_id":False,
    "server_id":False,
    "to_invoice":False,
    "table_id":False,
    "floor":False,
    "floor_id":False,
    "customer_count":1,
    "creation_date": "2020-02-10 10:10:10",
}
for i in range(2,10000):
    data['name'] = "Order 00126-003-%s" % i
    data['sequence_number'] = i
    data['uid'] = "00126-003-%s" % i
    res = po.create_from_ui([{'data':data}])
    print(res)


     
    
    "data":{"name":"Order 00126-001-0001","amount_paid":182.71,"amount_total":182.71,"amount_tax":31.71,"amount_return":0,"lines":[[0,0,{"qty":1,"price_unit":28,"price_subtotal":28,"price_subtotal_incl":33.88,"discount":0,"product_id":11414,"tax_ids":[[6,false,[5]]],"id":1,"pack_lot_ids":[],"note":""}],[0,0,{"qty":1,"price_unit":23,"price_subtotal":23,"price_subtotal_incl":27.830000000000002,"discount":0,"product_id":12511,"tax_ids":[[6,false,[5]]],"id":2,"pack_lot_ids":[],"note":""}],[0,0,{"qty":1,"price_unit":100,"price_subtotal":100,"price_subtotal_incl":121,"discount":0,"product_id":11808,"tax_ids":[[6,false,[5]]],"id":3,"pack_lot_ids":[],"note":""}]],"statement_ids":[[0,0,{"name":"2020-02-10 10:53:39","payment_method_id":4,"amount":182.71,"payment_status":"","ticket":"","card_type":"","transaction_id":""}]],"pos_session_id":126,"pricelist_id":66,"partner_id":false,"user_id":104,"employee_id":null,"uid":"00126-001-0001","sequence_number":1,"creation_date":"2020-02-10T10:53:39.957Z","fiscal_position_id":false,"server_id":false,"to_invoice":false,"table_id":false,"floor":false,"floor_id":false,"customer_count":1},"to_invoice":false}],false],"model":"pos.order","method":"create_from_ui","kwargs":{"context":{"lang":"en_US","tz":"CET","uid":104,"allowed_company_ids":[1]}}},"id":931457082}'