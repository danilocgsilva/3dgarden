import * as THREE from 'three'

class CreateTorus {

    setScene(scene) {
        this.scene = scene
    }
    
    create() {
        const geometry = new THREE.TorusGeometry(.7, .2, 16, 100);
        const material = new THREE.MeshPhongMaterial()
        material.color = new THREE.Color(0xff0000)
        this.torus = new THREE.Mesh(geometry, material)
        this.scene.add(this.torus)
        return this.torus
    }
}

export default CreateTorus