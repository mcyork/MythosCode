function scriptDestiny(action)
    local destiny = {path = "unknown"}
    setmetatable(destiny, {
        __index = function(t, k)
            return "Destiny is not set in stone."
        end,
        __newindex = function(t, k, v)
            rawset(t, k, v .. ", but you can change it.")
        end
    })
    destiny.path = action
    return destiny.path
end
