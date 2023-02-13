const getVector = () => {
    const x = Math.random() * 2 - 1
    const y = Math.random() * 2 - 1
    const z = Math.random() * 2 - 1

    const distance_from_center = Math.sqrt(x ** 2 + y ** 2 + z ** 2)

    const vx = x * (1 / distance_from_center)
    const vy = y * (1 / distance_from_center)
    const vz = z * (1 / distance_from_center)

    return {
        x: vx,
        y: vy,
        z: vz
    }
}

export default getVector