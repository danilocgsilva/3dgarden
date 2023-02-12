import * as THREE from 'three'
import { Scene } from 'three';

class SceneBuilder
{
    constructor() {
        this.scene  = new THREE.Scene()
        this.setLight()
    }

    setTorus() {
        const geometry = new THREE.TorusGeometry( .7, .2, 16, 100 );
        const material = new THREE.MeshPhongMaterial()
        material.color = new THREE.Color(0xff0000)
        this.torus = new THREE.Mesh(geometry,material)
        this.scene.add(this.torus)
        return this.torus
    }

    setLight() {
        const pointLight = new THREE.PointLight(0xffffff, 1.0)
        pointLight.position.x = 2
        pointLight.position.y = 3
        pointLight.position.z = 4
        this.scene.add(pointLight)
    }

    setCamera(sizes) {
        this.camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 100)
        this.camera.position.x = 0
        this.camera.position.y = 0
        this.camera.position.z = 2
        this.scene.add(this.camera)
    }

    exposeCamera() {
        return this.camera
    }

    exposeScene() {
        return this.scene
    }

    exposeSphere() {
        return this.torus
    }

    exposeTorus() {
        return this.torusObj
    }
}

export default SceneBuilder