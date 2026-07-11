local TARGETCONFIG = 1023
local MASK = {18, 53, 106, 68, 163, 470, 300, 816, 736, 384}

local function copyButtons(buttons)
    local copy = {}
    for i = 1, #buttons do
        copy[i] = buttons[i]
    end
    return copy
end

local function BFS(state)
    local queue = {}
    local head = 1
    local visited = {}

    queue[1] = { state = state, buttons = {}}
    visited[state] = true

    while head <= #queue do
        local curr = queue[head]
        head = head + 1

        if curr.state == TARGETCONFIG then return curr end

        for button = 1, 10 do
            local nextState = curr.state ~ MASK[button]
            if not visited[nextState] then
                visited[nextState] = true
                local nextButtons = copyButtons(curr.buttons)
                table.insert(nextButtons, button)
                table.insert(queue, { state = nextState, buttons = nextButtons })
            end
        end
    end
    return {state = state, buttons = {} }
end


local function main() 
    local state = 0
    local line = io.read()

    local pos = 1
    for v in line:gmatch("%d+") do
        if tonumber(v) == 1 then
            state = state | (1 << (pos - 1))
        end
        pos = pos + 1
    end

    if state == TARGETCONFIG then 
        print("0")
        return
    end 

    local ans = BFS(state)

    if #ans.buttons == 0 then
        print("-1")
        return
    end

    print(#ans.buttons)
    print(table.concat(ans.buttons, " "))
end

main()