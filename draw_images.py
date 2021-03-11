def clear_tile(c, x, y, l):
    return c.create_rectangle(x, y, x + l, y + l, fill = "white")

def create_void(func):
    def wrapper(*args, **kwargs):
        return (clear_tile(*args, **kwargs), func(*args, **kwargs))
    return wrapper

@create_void
def draw_void(c, x, y, l):
    pass

@create_void
def draw_base(c, x, y, l):
    i_d = (c, x, y, l)

    def create_block(c, x, y, l):
        _offset = max(x * 0.1, y * 0.1)
        _x0 = x + 0.1 * l; _x1 = x + l - l * 0.1
        _y0 = y + 0.4 * l; _y1 = y + l - l * 0.1
        return c.create_rectangle(_x0, _y0, _x1, _y1, fill="red", outline="red")

    def create_roof(c, x, y, l):
        points = {"left": {"x": x + 0.1 * l, "y": y + 0.4 * l},
                  "up": {"x": x + l / 2, "y": y + 0.1 * l},
                  "right": {"x": x + l * 0.9, "y": y + 0.4 * l}}
        return c.create_polygon([(points[i]["x"], points[i]["y"]) for i in points], fill="red", outline="red")

    
    return (create_block(*i_d), create_roof(*i_d))

@create_void
def draw_carryer(c, x, y, l):
    i_d = (c, x, y, l)
    return (c.create_arc(x + l * 0.1, y + l * 0.1, x + l * 0.9, y + l * 0.9, 
            start = 90, extent=180, fill="orange", outline="orange"),
            c.create_polygon(x + l * 0.5, y + l * 0.1, x + l * 0.5, y + l * 0.9, x + l * 0.9, y + l * 0.5,
            fill="orange", outline="orange"))
