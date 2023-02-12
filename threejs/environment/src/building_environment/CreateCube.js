import * as THREE from 'three'

class CreateCube
{
    setScene(scene) {
        this.scene = scene
    }

    create() {
        this.geometry = new THREE.BoxGeometry(0.5, 0.5, 0.5);
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
