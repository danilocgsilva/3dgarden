import * as THREE from 'three'

class SceneBuilder
{
    constructor(sizes, canvas) {
        this.sizes = sizes
        this.scene  = new THREE.Scene()
        this.setLight()
        this.camera = this.setCamera()
        this.renderer = this.setRenderer(canvas)
    }

    setGeoCreator(geoCreator) {
        this.geoCreator = geoCreator
        this.geoCreator.setScene(this.scene)
        return this
    }

    createGeo() {
        this.geoCreator.create()
    }

    setLight() {
        const pointLight = new THREE.PointLight(0xffffff, 1.0)
        pointLight.position.x = 2
        pointLight.position.y = 3
        pointLight.position.z = 4
        this.scene.add(pointLight)
    }

    setCamera() {
        const camera = new THREE.PerspectiveCamera(75, this.sizes.width / this.sizes.height, 0.1, 100)
        camera.position.x = 0
        camera.position.y = 0
        camera.position.z = 2
        this.scene.add(camera)
        return camera
    }

    setRenderer(canvas) {
        const renderer = new THREE.WebGLRenderer({canvas})
        renderer.setSize(this.sizes.width, this.sizes.height)
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
        return renderer
    }

    exposeCamera() {
        return this.camera
    }

    exposeScene() {
        return this.scene
    }

    exposeRenderer() {
        return this.renderer
    }

    exposeGeometry() {
        return this.geoCreator.exposeGeometry()
    }

    exposeMesh() {
        return this.geoCreator.exposeMesh()
    }
}

export default SceneBuilder