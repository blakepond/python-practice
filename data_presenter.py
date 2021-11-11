open_list = open("CupcakeInvoices.csv")

# for cupcake in open_list:
#     cupcake.strip()
#     cupcake = cupcake.split(",")
#     print(cupcake[2])


# for cupcake in open_list:
#     cupcake.strip()
#     cupcake = cupcake.split(",")
#     cupcake[3] = float(cupcake[3])
#     cupcake[4] = float(cupcake[4])
#     print("Invoice Total: ", cupcake[3] * cupcake[4])
invoice_sum = 0

for cupcake in open_list:
    cupcake.strip()
    cupcake = cupcake.split(",")
    cupcake[3] = float(cupcake[3])
    cupcake[4] = float(cupcake[4])
    invoice = cupcake[3] * cupcake[4]
    invoice_sum += invoice
    invoice_sum = round(invoice_sum, 2)
print(invoice_sum)

open_file.close()
