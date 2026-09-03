local DDD = {}
DDD[61] = "Brasilia"
DDD[71] = "Salvador"
DDD[11] = "Sao Paulo"
DDD[21] = "Rio de Janeiro"
DDD[32] = "Juiz de Fora"
DDD[19] = "Campinas"
DDD[27] = "Vitoria"
DDD[31] = "Belo Horizonte"

local num = tonumber(io.read())

if DDD[num] == nil then 
	print("DDD nao cadastrado")
else
	print(DDD[num])
end