local function main()
	while true do
        local line = io.read()
        if line == nil then 
        	break 
        end
        a, b = line:match("(%d+) (%d+)") 
        a, b = tonumber(a), tonumber(b)
        c = a ~ b
        print(c)
    end
end

main()