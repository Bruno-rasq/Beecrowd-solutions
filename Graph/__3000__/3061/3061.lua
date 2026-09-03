local DELTAS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

local function main() 

    local grid = {}
    local x, y = io.read("*n", "*n")

    for i=1, x do 
        local row = {}
        for j=1, y do
            row[j] = io.read("*n")
        end
        grid[i] = row
    end

    local blemishes = 0
    for i=1, x do
        for j=1, y do
            if grid[i][j] == 1 then 
                blemishes = blemishes + 1
                grid[i][j] = 0
                
                -- MARCA AS CÉLULAS ADJACENTES VALIDAS COMO VISITADAS
                local head = 1
                local queue = {{row=i, col=j}}
                while head <= #queue do
                    local curr = queue[head]
                    head = head + 1
                    for d=1, #DELTAS do
                        local nx = curr.row + DELTAS[d][1]
                        local ny = curr.col + DELTAS[d][2]
                        if nx >= 1 and nx <= x and ny >= 1 and ny <= y then 
                            if grid[nx][ny] == 1 then
                                grid[nx][ny] = 0
                                table.insert(queue, {row=nx, col=ny})
                            end
                        end
                    end
                end
            end
        end
    end
    
    print(blemishes)
end 

main()