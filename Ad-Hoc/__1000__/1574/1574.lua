local function main()
    local T = tonumber(io.read())
    
    for i=1, T do
        local x = 0 -- robo começa na origem x == 0 
        local instructions = {}
        local n = tonumber(io.read())
        
        for j=1, n do
            instruction = io.read()

            -- REPETIR NTH INSTRUÇÃO.
            if string.sub(instruction, 1, 7) == "SAME AS" then
                nth = instruction:match("SAME AS (%d+)")
                nth = tonumber(nth)
                instruction = instructions[nth]
            end
            
            if instruction == "LEFT" then x = x - 1 end
            if instruction == "RIGHT" then x = x + 1 end
            
            table.insert(instructions, instruction)
        end

        print(x)
    end
end

main()