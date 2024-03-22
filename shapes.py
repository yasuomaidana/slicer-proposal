import numpy as np


def line_from_points(xs: tuple[np.ndarray, np.ndarray], ys: tuple[np.ndarray, np.ndarray]) -> 'RawShape':
    x1, x2 = xs[0][1], xs[1][1]
    y1, y2 = ys[0][1], ys[1][1]
    return RawShape(np.array([x1, x2]), np.array([y1, y2]))


def generate_from_arc_line(theta: float, m: float, length: float, thetas: np.ndarray, r: float) -> 'RawShape':
    theta = thetas[np.argmin(np.abs(thetas - theta))]
    x1, y1 = r * np.cos(theta), r * np.sin(theta)
    dx = np.sign(m) * length / np.sqrt(1 + m ** 2)
    x2 = x1 + dx
    y2 = m * dx + y1
    return RawShape(np.array([x1, x2]), np.array([y1, y2]))


class RawShape:
    def __init__(self, x: np.ndarray, y: np.ndarray):
        self.x = x
        self.y = y

    def __reversed__(self):
        self.x = self.x[::-1]
        self.y = self.y[::-1]

    def __add__(self, other: 'RawShape') -> 'RawShape':
        x = []
        y = []
        use_self_first = len(self.x) >= len(other.x)
        xis, yis = (self.x, self.y) if use_self_first else (other.x, other.y)
        xjs, yjs = (other.x, other.y) if use_self_first else (self.x, self.y)
        dist = np.zeros_like(xis)
        for i, (xi, yi) in enumerate(zip(xis, yis)):
            dist[i] = np.isclose(np.min(np.sqrt((xjs - xi) ** 2 + (yjs - yi) ** 2)), 0)
        if sum(dist) == 0:
            x.extend(np.hstack((xis, xjs)))
            y.extend(np.hstack((yis, yjs)))
        elif sum(dist) == 1:
            if dist[0]:
                x.extend(np.hstack((xjs[:-1], xis)))
                y.extend(np.hstack((yjs[:-1], yis)))
            if dist[-1]:
                x.extend(np.hstack((xis, xjs[:-1])))
                y.extend(np.hstack((yis, yjs[:-1])))
        else:
            intersections = np.argwhere(dist).flatten()
            start, end = intersections[0], intersections[-1]
            x.extend(np.hstack((xis[0:start], xjs, xis[end:])))
            y.extend(np.hstack((yis[0:start], yjs, yis[end:])))
        return RawShape(np.array(x), np.array(y))

    def to_point_list(self) -> np.ndarray:
        return np.array([[i, j] for i, j in zip(self.x, self.y)])
