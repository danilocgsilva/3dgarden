import './style.css'
import SceneBuilder from './building_environment/SceneBuilder'
import CreateCube from './building_environment/CreateCube'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import enableResize from './building_environment/enableResize'
import getVector from './building_environment/getVector'

const cubesAmount = 10000

const canvas = document.querySelector('canvas.webgl')
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}
const sceneBuilder = new SceneBuilder(sizes, canvas)

const meshCollection = []

for (let i = 1; i <= cubesAmount; i++) {
    sceneBuilder.setGeoCreator(new CreateCube(0.05 , 0.05, 0.05))
    sceneBuilder.createGeo()
    meshCollection.push(
        {
           "mesh": sceneBuilder.exposeMesh(),
           "vector": getVector(),
           "intensity": Math.random()
        }
    )
}

const renderer = sceneBuilder.exposeRenderer()
const camera = sceneBuilder.exposeCamera()
const scene = sceneBuilder.exposeScene()

new OrbitControls(camera, renderer.domElement);

const tick = () => {

    meshCollection.forEach(meshData => {
        const { mesh, vector, intensity } = meshData
        mesh.translateX(vector.x * 0.002 * intensity)
        mesh.translateY(vector.y * 0.002 * intensity)
        mesh.translateZ(vector.z * 0.002 * intensity)
    });

    renderer.render(scene, camera)
    window.requestAnimationFrame(tick)
}
tick()

enableResize(sizes, camera, renderer)