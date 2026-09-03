local LIMIT = 100000

local function SUM(x, y)
    return x + y
end

local function SUB(x, y)
    return x - y
end

local function MUL(x, y)
    return x * y
end

local function DIV(x, y)
    if x % y == 0 then
        return x // y
    end
    return nil
end

local MATH = {SUM, SUB, MUL, DIV}

local function BFS(source, target, nums)

    if source == target then
        return 0
    end

    local queue = {
        {value = source, operations = 0}
    }

    local visited = {}
    visited[source] = true

    local head = 1

    while head <= #queue do
        local curr = queue[head]
        head = head + 1

        for i = 1, #nums do
            local a = nums[i]

            for j = 1, 4 do
                local nextValue = MATH[j](curr.value, a)

                if nextValue
                    and nextValue >= 1
                    and nextValue <= LIMIT
                    and not visited[nextValue] then

                    if nextValue == target then
                        return curr.operations + 1
                    end

                    visited[nextValue] = true
                    queue[#queue + 1] = {
                        value = nextValue,
                        operations = curr.operations + 1
                    }
                end
            end
        end
    end

    return -1
end

local source, target, n = io.read("*n", "*n", "*n")

local nums = {}
for i = 1, n do
    nums[i] = io.read("*n")
end

print(BFS(source, target, nums))