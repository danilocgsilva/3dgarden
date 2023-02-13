import * as THREE from 'three'

class CreateCube
{
    constructor(width = 0.5, length = 0.5, height = 0.5) {
        this.width = width
        this.length = length
        this.height = height
    }
    
    setScene(scene) {
        this.scene = scene
    }

    create() {
        this.geometry = new THREE.BoxGeometry(this.width, this.length, this.height);
        const material = new THREE.MeshPhongMaterial()
        material.color = new THREE.Color(0xff0000)
        this.mesh = new THREE.Mesh(this.geometry, material);
        this.scene.add(this.mesh);
    }

    exposeGeometry() {
        return this.geometry
    }

    exposeMesh() {
        return this.mesh
    }
}

export default CreateCube
